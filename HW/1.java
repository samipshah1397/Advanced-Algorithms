//Author @ Samip
#include<iostream>
using namespace std;

int partition(int a[], int start,int end)
{
  int pivot,i,j,temp;
  pivot = a[end]; 
  i= start-1;
  for(j = start; j<= end-1; j++)
  {
    if(a[j] <= pivot ) {
      i++;
      temp = a[i]; //swap a[i] and a[j]
      a[i] = a[j];
      a[j] = temp;
    }
  }
  temp = a[i+1]; //swap a[i+1] and a[end]/pivot
  a[i+1] = a[end];
  a[end] = temp;
  return i+1; //returning correct/new index of pivot
}

int randomized_partition(int a[], int start,int end)
{
  int size=end-start+1;
  srand(time(NULL));
  int i=rand() % (size) + start;

  int temp= a[i]; //place random pivot at the end 
  a[i]=a[end];
  a[end]=temp;
  return partition(a,start,end);
}

void randomized_quicksort(int a[],int start,int end)
{
  if( start < end ){
    int pivot_loc= randomized_partition(a,start,end);
    randomized_quicksort(a,start,pivot_loc-1);
    randomized_quicksort(a,pivot_loc+1,end);
  }
}



int main()
{
  int n,i,j;
  cout<<"Enter total number of elements/size: ";
  cin>>n;
  int arr[n];
  cout<<"Enter numbers: ";
  for(i = 0;i< n; i++) //Enter [[5 6 8 10 11 13 8 8 3 5 2 11 8]]
    cin>>arr[i];
  randomized_quicksort(arr,0,n-1);
  cout<<"Array sorted in increasing order using randomized quicksort: "<< endl;
  for(i = 0;i< n; i++)
    cout<< arr[i]<<" ";
  return 0;
}
