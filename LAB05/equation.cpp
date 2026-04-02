#include <iostream>
using namespace std;

double func(int n) {
    if (n == 0)
        return 0;

    double prev = func(n - 1);

    if (n % 2 == 1)
        return prev + (1.0 / n);
    else
        return prev - (1.0 / n);
}

int main() {
    int n;
    cout << "n: ";
    cin >> n;

    cout << func(n) << endl;

    return 0;
}
