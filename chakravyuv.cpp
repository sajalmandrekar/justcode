/*
This code outputs nos in a spiral order
*/

#include<iomanip>
#include <iostream>
using namespace std;

int main()
{
  int i=0,j=0,count,limit,n,val=1;
  cin>>n;
  int a[n][n];
  for(limit = n-1; limit>0; limit-=2,i++,j++)
  {
    for(count = 1; count <=limit ; count++) a[i][j++] = val++;
     
    for(count = 1; count <=limit ; count++) a[i++][j] = val++;
     
    for(count = 1; count <=limit ; count++) a[i][j--] = val++;
     
    for(count = 1; count <=limit ; count++) a[i--][j] = val++;
  }    

  if(!limit) a[i][j] = val;

  // Displaying the 2D array
  for(i=0;i<=n-1;i++)
  {
    for(j=0;j<=n-1;j++)
    cout<<setw(5)<<a[i][j];
    cout<<endl<<endl; 
  }

  return 0;
}
