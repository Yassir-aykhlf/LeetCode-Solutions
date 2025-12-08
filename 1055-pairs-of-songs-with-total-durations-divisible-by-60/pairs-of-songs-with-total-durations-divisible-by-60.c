int numPairsDivisibleBy60(int* time, int timeSize) {
    int rems[60] = {0};
    int count = 0;
    for (int i = 0; i < timeSize; ++i) {
        int cur_rem = time[i] % 60;
        int target_rem = (60 - cur_rem) % 60;
        count += rems[target_rem];
        rems[cur_rem] += 1;
    }
    return count;
}