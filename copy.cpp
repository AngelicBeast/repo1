#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
typedef long long ll;
using namespace std;

int binary_search(vector<long long> &arr, long long x)
{
    int low = 0;
    int high = arr.size() - 1;
    int mid = 0;

    while (low <= high)
    {
        mid = (high + low) / 2;

        // If x is greater, ignore left half
        if (arr[mid] < x)
        {
            low = mid + 1;
        }
        // If x is smaller, ignore right half
        else if (arr[mid] > x)
        {
            high = mid - 1;
        }
        // means x is present at mid
        else
        {
            return mid;
        }
    }

    // If we reach here, then the element was not present
    return -1;
}

int main()
{
    cout << ((((ll)pow(323, 7) - 1) / 322)) << endl;
    vector<long long> l;
    for (int k = 2; k < pow(10, 6); k++)
    {
        int x = 3;
        while ((pow(k, x) - 1) / (k - 1) <= pow(10, 18))
        {
            if (k == 323)
            {
                cout << (((ll)pow(k, x) - 1) / (k - 1)) - 1139099823644293 << " ";
                cout << " <" << (((ll)pow(k, x) - 1) / (k - 1)) << ">";
            }
            l.push_back((ll)(pow(k, x) - 1) / (k - 1));
            x++;
        }
    }
    sort(l.begin(), l.end());
    /*cout<<binary_search(l,5772870588346120)<<" "<<l.size()<<endl;*/
    ll t;
    cin >> t;
    for (ll _ = 0; _ < t; _++)
    {
        ll u = 0;
        ll n;
        cin >> n;
        if (n == 1 or n == 3)
        {
            cout << "NO" << endl;
            continue;
        }
        /*if(t==10000 and _==1){
            u=n;
        }
        if(_==48 and u==1111111111111111){
            cout<<n<<endl;
            continue;
        }*/
        long long k = sqrt(4 * n - 3);
        if (k * k == 4 * n - 3 or (k - 1) * (k - 1) == 4 * n - 3 or (k + 1) * (k + 1) == 4 * n - 3)
        {
            cout << "YES" << endl;
            continue;
        }
        else
        {
            if (binary_search(l, n) == -1)
            {
                cout << "NO" << endl;
                continue;
            }
            else
            {
                cout << "YES" << endl;
                continue;
            }
        }
    }

    return 0;
}