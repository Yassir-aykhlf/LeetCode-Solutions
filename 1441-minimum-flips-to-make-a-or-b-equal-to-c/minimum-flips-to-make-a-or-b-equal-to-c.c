int minFlips(int a, int b, int c){
    int count = 0;
    for (int i = 0; i < 32; i++) {
        bool a_ = a & 1;
        bool b_ = b & 1;
        bool c_ = c & 1;
        if (c_) {
            if (!a_ && !b_) {
                count += 1;
            }
        }
        else {
            if (a_ && b_) {
                count += 2;
            }
            else if (a_ || b_) {
                count += 1;
            }
        }
        a >>= 1;
        b >>= 1;
        c >>= 1;
    }
    return count;
}