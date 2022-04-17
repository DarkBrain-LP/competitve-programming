#include <bits/stdc++.h>
#include <ctime>

using namespace std;

bool leap(int year){
    return (!(year & 3) && ((year % 25) || !(year & 15)));
}

int getMonthDays(int year, int month){
    return (month==2)?(leap(year)?29:28)/*februaryDays(year)*/:(( (month%2 == 0 && month <= 7) || (month%2 != 0 && month > 7) )?30:31) ;
}

int main(){
    

    time_t now = time(0);

    tm *ltm = localtime(&now);
    //int y = 1900 + ltm->tm_year, m = 1 + ltm->tm_mon, d = ltm->tm_mday, nbDays = 1975800,  n = nbDays, yearDay = 1 + ltm->tm_yday;
    int y = 1900 + ltm->tm_year; // current year
    int m = 1 + ltm->tm_mon; // current month
    int d = ltm->tm_mday; // current day of the month
    int yearDay = 1 + ltm->tm_yday; // the number the corresponds to the current date, beginning from Jan 1st
    
    int  nbDays = 1975800;
    int  n = nbDays;

    cout << "Current Date : " <<  m << "-" << d << "-" << y << '\n';
    cout << "Enter the number of days : ";
    cin >> nbDays;
    n = nbDays;
    
    int remainingDay = (leap(y)?366:365) - yearDay ; // days before end of year
    
    if(n >= remainingDay + 1){
        // Here i set the date to 1st Jan of the next year
        y += 1; m = 1; d = 1; n -= (remainingDay + 1);
    }

    int yearDays = 0;
    yearDays = (leap(y)?366:365) ;

    while( n > yearDays){
        // Here i substract as many as possible the number of year in the entered day
        n -= yearDays ;
        y +=1;
        yearDays = (leap(y)?366:365) ;
    }

    int monthDays = 0; // The number of days of a given month (Jan -> 32; Feb -> 28/29 ...)

    for(int i = m; i <= 12 ; i++){
        monthDays = getMonthDays(y, i) ;
        // if the remaining days before the end of the month is less than n, we can go to the next month
        // so i substract that remaining days from n, adding a new month an setting the day of that month at the 1st
        if(n > monthDays - d){
            n = n - (monthDays - d) - 1;
            d = 1;
            m += 1;
        } else{
            break;
        }
        
    }

    d += n; // adding the remaining days(can't take us to the next month)
    
    cout << "After " << nbDays << ", the date should be " ;
    cout << m << '-' << d << '-' << y << '\n';
}