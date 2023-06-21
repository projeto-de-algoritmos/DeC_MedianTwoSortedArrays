#include <bits/stdc++.h>

using namespace std;

using ll = long long;

long long Pow(long long x, long long y) {
    if(y == 0)
        return 1;
    if(y&1)
        return x*Pow(x*x, y/2);
    else
        return Pow(x*x, y/2);
}

int main() {
    string line;
    while (getline(cin, line)) {
        ll x;

        stringstream ss(line);
        ss >> x;

        vector<ll> c;
        ll num;
        getline(cin, line);
        stringstream sss(line);
        while (sss >> num) {
            c.push_back(num);
        }

        ll n = c.size();
        ll ans = 0;
        for (ll i = 0; i < n - 1; i++) {
            ans += c[i] * (n - i - 1) * Pow(x, n - i - 2);
        }
        cout << ans << endl;
    }
    return 0;
}
