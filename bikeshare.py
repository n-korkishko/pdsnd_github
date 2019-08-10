import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('Would you like to see data for Chicago, New York City, or Washington? \n ')
        city=city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Something went wrong...")

    while True:
        month= input('Which month? January, February, March, April, May, June or all? \n')
        month=month.lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may','june']:
            break
        else:
            print("Something went wrong...")
    while True:
        day= input('Which day of week? You can also pick all \n ')
        day=day.lower()
        if day in ['all', 'sunday', 'monday', 'tuesday', 'wendnesday', 'thuesday','friday','saturday']:
            break
        else:
            print("Something went wrong...")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
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
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    # not to do the most frequent month search if user selected the particular one
    if len(df['month'].unique().tolist()) > 1:
        popular_month = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        print('Most Frequent month:', months[popular_month-1])
    # display the most common day of week
    # not to do the most frequent month search if user selected the particular one
    if len(df['day_of_week'].unique().tolist()) > 1:
        popular_day = df['day_of_week'].mode()[0]
        print('Most Frequent day', popular_day)
    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['start+end']=df['Start Station']+ ' -> ' + df['End Station']
    popular_combination=df['start+end'].mode()[0]
    print('Most popular trip:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)


    # display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    print('Average travel time:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(df['User Type'].unique())
    print('\nCounts of user types: \n', user_types)

    # Display counts of gender
    try:
        Gender = df['Gender'].value_counts()
        print('\nCounts of Gender: \n', Gender)
    except:
        KeyError: 'Gender'


    # Display earliest, most recent, and most common year of birth
    try:
        earliest=int(df['Birth Year'].min())
        print('\nEarliest year of birth: ', earliest)
        yangest=int(df['Birth Year'].max())
        print('Youngest year of birth: ', yangest)
        most_common=int(df['Birth Year'].mode())
        print('Most common year of birth: ', most_common)
    except:
        KeyError: 'Birth Year'


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
