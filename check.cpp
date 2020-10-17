#include <iostream>
using namespace std;
void math(int x,int y,string word){
 int result = x+y;
 cout<<word<<endl;
  cout<<"your result is "<< result<<endl;
}

int output(string word){
   string Message;
   cout<<word<<endl;
    cout<<"Hello world "<<endl;
    cout<<"What would you like to say to the world?"<<endl;
    cin>>Message;
    cout<<"Hello world, please "<<Message<<endl;
    return 0;
  }
  int main(){
  string word = "I am here first";
  //output(word);
  int x = 5;
  int y = 3;
  math(x,y,word);
  return 0;
}
