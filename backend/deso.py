npm i deso-protocol 
 import Deso from 'deso-protocol';
const deso = new Deso();
const request = {
  "SenderPublicKeyBase58Check": null,
  "RecipientPublicKeyOrUsername": "BC1YLheA3NepQ8Zohcf5ApY6sYQee9aPJCPY6m3u6XxCL57Asix5peY",
  "AmountNanos": 1,
  "MinFeeRateNanosPerKB": 1000
};
 const response = await deso.wallet.sendDesoRequest(request);
 import Deso from 'deso-protocol';
const deso = new Deso();
const request = {
  "UpdaterPublicKeyBase58Check": null,
  "CreatorPublicKeyBase58Check": "BC1YLheA3NepQ8Zohcf5ApY6sYQee9aPJCPY6m3u6XxCL57Asix5peY",
  "OperationType": "buy",
  "DeSoToSellNanos": 10001,
  "MinFeeRateNanosPerKB": 1000
};
 const response = await deso.wallet.buyOrSellCreatorCoin(request);
  import Deso from 'deso-protocol';
const deso = new Deso();
const request = {
  "NumToFetch": 50,
  "PublicKeyBase58Check": "BC1YLjMYu2ahUtWgSX34cNLeM9BM9y37cqXzxAjbvPfbxppDh16Jwog",
  "FetchStartIndex": 100
};
 const response = await deso.notifications.getNotifications(request);
  import Deso from 'deso-protocol';
const deso = new Deso();
const request = {
  "PublicKeyBase58Check": "BC1YLheA3NepQ8Zohcf5ApY6sYQee9aPJCPY6m3u6XxCL57Asix5peY"
};
 const response = await deso.notification.getUnreadNotificationsCount(request);
  import Deso from 'deso-protocol';
const deso = new Deso();
const request = 4354315e08ce066e0487ef85d2476579bfe6a8c0c8d3979374085dcae753b04d;
 const response = await deso.transaction.getTransaction(request);
