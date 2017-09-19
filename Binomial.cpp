#include<iostream>
#include<vector>
#include <algorithm>
#include <climits>

using namespace std;
//小数阶乘，直接递归
long int smallfactorial(int n)
{
    return (n==0 || n==1) ? 1: n*smallfactorial(n-1);
}

//排列计算A(n,k)
long long int rankA(int n, int k)
{
    unsigned long long int sum=1;
    while(k>0)
    {
        sum *= (n-k+1);
        k--;
    }
    return sum;
}

//组合计算C(n, k)
unsigned long long int binomial(unsigned n, unsigned k)
{
    unsigned long long int c=1;
    if(k>n-k)
        k=n-k;
    for(int i=1; i<=k; i++,n--)
    {
        if(c/i > ULLONG_MAX / n)
            return 0;
        c = c/i * n + c%i *n /i;
    }
    return c;
}

// 计算大数的阶乘，结果保存在vector中
void factorial(const int n, const int k, vector<int> &fac)
{
    fac.push_back(1);
    if(n==0 || n==1)
        return;
    //从2开始，依次乘i，每次更新vector
    for(int i=2; i<=k; i++)
    {
        int reminder=0, addition=0;
        int lens = fac.size();
        vector<int> tmp;
        for(int j=0; j<lens-1;j++)
        {
            reminder = (i*fac[j] + addition) %10;   //当前位的余数
            addition = (i*fac[j] + addition) /10;    //当前位的进位数
            tmp.push_back(reminder);
        }
        int last = i*fac[lens-1] + addition;  //最高位更新
        while (last!=0) {
            tmp.push_back(last%10);
            last /= 10;
        }
        fac.swap(tmp);
    }
    std::reverse(fac.begin(), fac.end());    //翻转vector，使得高位在前，低位在后
}


int main()
{
    int length=11;
    vector<int> fac;
    factorial(length, 10, fac);
    for(auto x : fac)
        cout<<x;
    cout << endl;
    cout << rankA(10, 5)<<endl;
    cout << binomial(100, 10)<<endl;
    return 0;
}
