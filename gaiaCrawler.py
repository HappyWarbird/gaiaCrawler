import requests

tokenid = 0
start = 0

while tokenid == 0:
  url = 'https://marketplace-graphql.skymavis.com/graphql'
  data = {"operationName":"GetERC721TokensList","variables":{"from":0,"auctionType":"All","size":50,"sort":"PriceAsc","criteria":[{"name":"type","values":["unrevealed"]}],"rangeCriteria":[],"tokenAddress":"0xd78efaec85c1a4f42e6edb7209067702a2be8c90"},"query":"query GetERC721TokensList($tokenAddress: String!, $owner: String, $auctionType: AuctionType, $criteria: [SearchCriteria!], $from: Int!, $size: Int!, $sort: SortBy, $name: String, $priceRange: InputRange, $rangeCriteria: [RangeSearchCriteria!]) {\n  erc721Tokens(\n    tokenAddress: $tokenAddress\n    owner: $owner\n    auctionType: $auctionType\n    criteria: $criteria\n    from: $from\n    size: $size\n    sort: $sort\n    name: $name\n    priceRange: $priceRange\n    rangeCriteria: $rangeCriteria\n  ) {\n    total\n    results {\n      ...Erc721TokenBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Erc721TokenBrief on Erc721 {\n  tokenAddress\n  tokenId\n  owner\n  name\n  order {\n    ...OrderInfo\n    __typename\n  }\n  image\n  cdnImage\n  video\n  isLocked\n  attributes\n  traitDistribution {\n    ...TokenTrait\n    __typename\n  }\n  collectionMetadata\n  ownerProfile {\n    name\n    accountId\n    __typename\n  }\n  __typename\n}\n\nfragment OrderInfo on Order {\n  id\n  maker\n  kind\n  assets {\n    ...AssetInfo\n    __typename\n  }\n  expiredAt\n  paymentToken\n  startedAt\n  basePrice\n  expectedState\n  nonce\n  marketFeePercentage\n  signature\n  hash\n  duration\n  timeLeft\n  currentPrice\n  suggestedPrice\n  makerProfile {\n    ...PublicProfileBrief\n    __typename\n  }\n  orderStatus\n  orderQuantity {\n    orderId\n    quantity\n    remainingQuantity\n    availableQuantity\n    __typename\n  }\n  __typename\n}\n\nfragment AssetInfo on Asset {\n  erc\n  address\n  id\n  quantity\n  __typename\n}\n\nfragment PublicProfileBrief on PublicProfile {\n  accountId\n  addresses {\n    ...Addresses\n    __typename\n  }\n  activated\n  name\n  __typename\n}\n\nfragment Addresses on NetAddresses {\n  ethereum\n  ronin\n  __typename\n}\n\nfragment TokenTrait on TokenTrait {\n  key\n  value\n  count\n  percentage\n  displayType\n  __typename\n}\n"}
  data['variables']['from'] = start
  response = requests.post(url, json=data)
  response = response.json()
  for i in response['data']['erc721Tokens']['results']:
    kaidroUrl = 'https://kaidro.com/nft/journal_nft/'+ i['tokenId'] +'.json'
    kaidroResp = requests.get(kaidroUrl)
    kaidroResp = kaidroResp.json()
    if kaidroResp['properties']['type'] == 'gaias':
      tokenid = i['tokenId']
  print('TokenID ' + str(tokenid) + ' after ' + str(start))
  start = start + 50
print('Geil, ech ha es Gaia Journal gfonde!!! https://marketplace.skymavis.com/collections/0xd78efaec85c1a4f42e6edb7209067702a2be8c90/' + str(tokenid))
