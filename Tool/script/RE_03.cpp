#include <iostream>
using namespace std;
int main()
{
    int cipher[33] = {0xe7, 0x99, 0xdb, 0xf6, 0x98, 0xda, 0xf6, 0xda, 0x99, 0xf6, 0xe4, 0x9d, 0xce, 0x98, 0xca};
    for (int i = 0; i < 15; i++)
    {
        cout << char(cipher[i] ^ 0xa9);
    }
}