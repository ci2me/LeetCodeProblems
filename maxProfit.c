// // easy method, terrible time complexity
// int maxProfit(int* prices, int pricesSize) {
//     int i = 0;
//     int j = 0;
//     int max = 0;
//     int profit;
//     int profitIdx = 0;

//     for(i=0; i < pricesSize;i++){
//         for(j=i+1;j<pricesSize;j++){
//             if (prices[j] > prices[i]){
//                 profit = prices[j] - prices[i];
//                 if (profit > max){
//                     max = profit;
//                 }
//             }
//         }
//     }
//     // return sizeof(profitIdx);
//     return max;
//     // return profit;
// }

// optimised window approach
int maxProfit(int* prices, int pricesSize) {
    int i = 0;
    int j = 1;
    int profit = 0;
    int max = 0;

    while (j < pricesSize){
        if (prices[i] >= prices[j]){
            i = j;
        }
        else{
            profit = prices[j] - prices[i];
            if(profit > max){
                max = profit;
            }
        }
        j++;
    }
    return max;
}
