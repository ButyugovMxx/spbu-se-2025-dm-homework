#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<string> a;
vector<string> cur;

void gen(int pos) {
    // если набрали k элементов — печатаем
    if ((int)cur.size() == k) {
        for (int i = 0; i < k; i++) {
            if (i) cout << ' ';
            cout << cur[i];
        }
        cout << '\n';
        return;
    }

    // если элементов больше нет — выходим
    if (pos == n) return;

    // берём текущий элемент
    cur.push_back(a[pos]);
    gen(pos + 1);
    cur.pop_back();

    // не берём текущий элемент
    gen(pos + 1);
}

int main() {
    cin >> n >> k;
    a.resize(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    gen(0);
    cout << '\n';
}
