static int x_sum( const auto& freq, int k, int x){
    auto freq2=freq;// freq2 is a copy of freq
    // sort freq2 with greater ordering
    sort(freq2.begin(), freq2.end(), greater<int2>());
    int sum=0;
    for (int i=0; i<x; i++){// compute x-sum
        auto [f, num]=freq2[i];
        if (f==0) break;
        sum+=num*f;
    }
    return sum;
}