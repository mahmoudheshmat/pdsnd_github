import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
print('\nHello! Let\'s explore some US bikeshare data!')
print('-'*40)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # first get user input for city (chicago, new york city, washington).
    # while loop to handle invalid inputs
    # lower function to accept all city input formats
    while True:
        city = input("\nWhich city ? New York City, Chicago or Washington?\n").lower()
        if city in ('new york city', 'chicago', 'washington'):
            break
        else:
            print("Sorry, please choose one city of above.")
            continue
            # second get user input for month (all, january, february, ... , june)
    # while loop to handle invalid inputs
    # lower function to accept all month input formats
    while True:
        month = input("\nWhich month ? January, February, March, April, May, June or type 'all'.\n").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("Sorry, please choose one month of above or all.")
            continue
            # third get user input for day of week (all, monday, tuesday, ... sunday)
    # while loop to handle invalid inputs
    # lower function to accept all day input formats
    while True:
        day = input(
            "\nWhich day? Choose: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'.\n")
        if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            break
        else:
            print("Sorry, please choose one day of above or all .")
            continue
    print('-' * 40)
    # return user inputs
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def city_data(df):
    """Viewing some properties of selected data."""
    # start by viewing the colums of the dataset!
    print('\n viewing the colums in this city dataset! ...\n')
    print(df.columns)
    # start by viewing the describe of the dataset!
    print('\n viewing the describe of this city dataset! ...\n')
    print(df.describe())
    # start by viewing the first few rows of the dataset!
    print('\n viewing the first few rows in this city dataset! ...\n')
    print(df.head())
    print('-' * 40)


def time_stats(df):
    """1- Popular times of travel ."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month:', popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most common day of week:', popular_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('most common hour of day:', popular_hour)
    print('-' * 40)


def station_stats(df):
    """2- Popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    # display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('most common start station:', Start_Station)
    # display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print('\nmost common end station:', End_Station)
    # display most frequent combination of start station and end station trip
    Combination_Station = df['Start Station'] + " to " + df['End Station']
    df['Combination_Station'] = Combination_Station
    Combination_Station = df['Combination_Station'].mode()[0]
    print('\nmost common trip from start to end:', Combination_Station)
    print('-' * 40)

def trip_duration_stats(df):
    """3-Trip duration."""
    print('\nCalculating Trip Duration...\n')
    # display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('total travel time:', Total_Travel_Time / 86400, " Days")
    # display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean()
    print('average travel time:', Average_Travel_Time / 60, " Minutes")
    # display max travel time
    Max_Travel_Time = df['Trip Duration'].max()
    print('max travel time:', Max_Travel_Time / 60, " Minutes")
    print('-' * 40)


def user_stats(df, city):
    """4-User info."""
    print('\nCalculating User Stats...\n')
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of each user type:\n', user_types)
    # Display sum of all user types
    total_user_types = sum(user_types)
    print('sum of all user types:', total_user_types)
    # Display counts of gender
    if city in ('new york city', 'chicago'):
        gender_types = df['Gender'].value_counts()
        print('\ncounts of each gender:\n', gender_types)
        # Display sum of all genders
        total_genders = sum(gender_types)
        print('sum of all genders:', total_genders)
        # Display earliest, most recent, and most common year of birth
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('\nMost Common Year:', Most_Common_Year)
    else:
        print(
            "\nGender Types,Total Genders,Earliest Year,Most Recent Year,Most Common Year:\nsorry this data not available now for washington city.")
    print('-' * 40)
def raw_data(df):
    """5-some raw of data."""
    # Ask user if he want to see some lines of data from the filtered dataset.
    # while loop to handle invalid inputs
    # lower function to accept all input formats
    i = 0
    x = 5
    while True:
        raw_data=input('\nWould you like to see raw of data? Enter yes or no.\n')
        if raw_data.lower()=='yes':
            # Display some lines of data if answer is yes
            print(df.iloc[i:x])
            i+=5
            x+=5
            print('-'*40)
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        city_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()