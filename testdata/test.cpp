#include <bits/stdc++.h>
#define pir pair<int,int>
using namespace std;

int mini = INT32_MAX;
pir ans[10];
int a[10];
// 1:267285, 2:919, 3:356, 4:1451, 5:
pir com[50] = 
{
    {0,1}, 
    {0,2}, {1,2}, 
    {0,3}, {1,3}, {2,3}, 
    {0,4}, {1,4}, {2,4}, {3,4}, 
    {0,5}, {1,5}, {2,5}, {3,5}, {4,5},
    {0,6}, {1,6}, {2,6}, {3,6}, {4,6}, {5,6},
    {0,7}, {1,7}, {2,7}, {3,7}, {4,7}, {5,7}, {6,7},
    {0,8}, {1,8}, {2,8}, {3,8}, {4,8}, {5,8}, {6,8}, {7,8},
    {0,9}, {1,9}, {2,9}, {3,9}, {4,9}, {5,9}, {6,9}, {7,9}, {8,9} 
};

void recur(int len, int sum, int arr[10], pir prog[10])
{
    //system("pause");
    if (len == 1)
    {
        if(mini > sum)
        {
            mini = sum;
            for (int i=0;i<9;i++)
                ans[i].first = prog[i].first, ans[i].second = prog[i].second;
        }
        return;
    }
    if (sum > mini)
        return;
    vector <int> list;
    for (int i = 0; i < (len-1)*len/2; i++) 
    {
        int ind = 0;
        int input[10];
        for(int j=0;j<len;j++)
        {
            if(j != com[i].first && j != com[i].second)
            {
                input[ind] = arr[j];
                ind++;
            }
        }
        input[ind] = arr[com[i].first] + arr[com[i].second];
        prog[10-len].first = arr[com[i].first], prog[10-len].second = arr[com[i].second];

        //recur(len-1, sum + arr[com[i].first]*arr[com[i].second], input, prog);//1 
        //recur(len-1, sum + arr[com[i].first]+arr[com[i].second], input, prog);//2 
        //recur(len-1, sum + min(arr[com[i].first],arr[com[i].second]), input, prog);//3 
        //recur(len-1, sum + max(arr[com[i].first],arr[com[i].second]), input, prog);//4 
        recur(len-1, sum + max(arr[com[i].first],arr[com[i].second]) - min(arr[com[i].first],arr[com[i].second]), input, prog);//5 
    }
    return;
}

int main()
{
    for (int i=0;i<10;i++)
        cin>>a[i];
    pir tp[10];
    recur(10,0,a,tp);
    cout<<mini<<'\n';
    for (int i=0;i<9;i++)
        printf("%d %d\n", ans[i].first, ans[i].second);
}