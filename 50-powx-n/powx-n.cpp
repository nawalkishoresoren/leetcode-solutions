class Solution {
public:
    double power(double x, long long n)
    {
        if (n == 0) return 1;
        if (n == 1) return x;
        return (n % 2 == 0) ? power(x * x, n / 2) : x * power(x * x, n / 2);
    }
    double myPow(double x, long long n)
    {
        if (n < 0)
            return 1 / power(x, -n);
        return power(x, n);
        
    }
};