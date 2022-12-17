//============================================================================
// Name        : hammingcode_31135.cpp
// Author      : Sanika Inamdar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main()
{
    //cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
    int m = 0; // no. of bits
    int bi;
    cout << "Enter binary value:" << endl;
    cin >> bi;
    int b = bi;
    while (b != 0)
    {
        b = b / 10;
        m++;
    }
    int r = 0;
    for (int i = 0; i <= m; i++)
    {
        if (pow(2, i) >= (m + i + 1))
        {
            r = i;
            break;
        }
    }
    int arr[20];
    // vector<int>arr;
    arr[0] = -1;
    for (int i = 0; i < r; i++)
    {
        int in = pow(2, i);
        arr[in] = -1;
    }
    for (int i = 1; i < m + r + 1; i++)
    {
        if (arr[i] != -1)
        {
            int digit = bi % 10;
            arr[i] = digit;
            bi = bi / 10;
        }
    }
    cout << "Array is: " << endl;
    for (int i = m + r; i >= 1; i--)
    {
        cout << arr[i] << " ";
    }
    int count = 0;
    for (int i = 1; i <= r; i++)
    {
        int p = pow(2, i - 1);
        cout << "for r=: " << p << endl;
        for (int j = p; j < m + r + 1; j++)
        {
            cout << "the position of j: ";
            if (arr[j] == 1)
            {
                count++;
                cout << j << " ";
            }

            if ((j + 1) % p == 0)
            {
                j = j + p;
            }
        }
        cout << "count of r" << p << "is :" << count << endl;
        int ind = pow(2, i - 1);
        if (count % 2 == 0)
        {
            arr[ind] = 0;
        }
        else
            arr[ind] = 1;
        count = 0;
    }
    cout << "Array is: " << endl;
    for (int i = m + r; i >= 1; i--)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << m << " " << r;
    return 0;
}
