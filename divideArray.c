// // easy solution
// bool divideArray(int* nums, int numsSize) {
//     int x;
//     // bool ans = true;
//     for (int x = 1;x <= 500; x++){
//         int count = 0;
//         for(int i = 0; i< numsSize; i++){
//             if (nums[i] == x){
//                 count++;
//             }
//         }
//         if(count % 2 != 0){
//             return false;
//         }
//     }
//     return true;
//}

// optimal solution
bool divideArray(int* nums, int numsSize){
    int counters[500];
    for(int i = 0; i < numsSize;i++){
        // smallest number is 1, index for each number
        // will be between 0 and 499
        counters[nums[i] - 1]++;
    }

    for(int i; i< 500; i++){
        // check if each value can be put in pair
        if (counters[i]%2==1){
            return false;
        }
    }
    return true;
}
