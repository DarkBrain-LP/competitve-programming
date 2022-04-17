#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input2.txt", "r", stdin); // reading the input from the input2.txt
    freopen("output2.txt", "w", stdout); // outputing in the outpou2.txt

    int n = 0, count = 0;
    string currentHashtag = "";
    bool found = false;
    unordered_map<string, int> hashtags ; // map structure for hashtags and their apparition number within 60 min

    cin >> n;

    for(int i = 0; i < n; i++){
        // Reading the current hashtag
        cin >> currentHashtag;
        // adding it to the data structure. By doing hashtags[currentHashtag], the values is 0
        // so the next line creates the key currentHashtag if it doesn't exits and/or increments it
        hashtags[currentHashtag] += 1; 
        count ++;

        if(hashtags[currentHashtag] == 40){
            found = true;
            cout << currentHashtag;
            break;
        }

        if(count == 60){
            count = 1;
            for(auto j : hashtags){
                j.second = 0;
            }
        }

    }
    if(!found){
        cout << "Pas de trending topic" << "\n" ;
    }
    
}