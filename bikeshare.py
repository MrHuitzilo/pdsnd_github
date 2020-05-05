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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('What city would you like to explore?\nChicago, New York City, Washington? ').lower()
        if city not in ('chicago','new york city', 'washington'):
            print('\nOops! That didn\'t look like a city option... Why don\'t you try again and enter "Chicago", "New York City" or "Washington" (without quotes)')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhat month would you like to take a look at?\nEnter any month from January through June or enter All for all months: ').lower()
        if month not in ('all','january', 'february','march','april','may', 'june'):
            print('\nThat didn\'t look right... Try entering the full name of the month such as "April" or enter "All" for all months (without quotes).')
            print('Keep in mind it MUST be a month from "January" through "June" or it can be "All".')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nLastly, what day of the week is to be pulled?\nEnter any day of the week, such as Monday: ').lower()
        if day not in('monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday'):
            print('\nThad didn\'t look like a day of the week...Try entering the name of day, such as "Monday" (without quotes).')
        else:
            break
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
        df - Pandas DataFrame containing city data filtered by month and day
    """

     # loading the data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converting the start time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extracting hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        day_of_week = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
        df = df[df['month'] == month]

        # filter by weekday
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    c_month = df['month'].mode()[0]
    print('Most common month: ', c_month)

    # TO DO: display the most common day of week
    c_dow = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', c_dow)

    # TO DO: display the most common start hour
    c_hour = df['hour'].mode()[0]
    print ('Most common hour: ', c_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    c_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', c_start_station)

    # TO DO: display most commonly used end station
    c_end_station = df['End Station'].mode()[0]
    print('Most common end station: ', c_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    c_stations = (df['Start Station'] + ' -- AND -- ' + df['End Station']).mode()[0]
    print('Most common combination of start and end station: ', c_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tt_total = df['Trip Duration'].sum()
    print('Total travel time during selected time frame: ',tt_total/60, ' mins')

    # TO DO: display mean travel time
    tt_mean = df['Trip Duration'].mean()
    print('Mean of travel time during selected time frame: ',tt_mean/60, ' mins')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ut_count = df.groupby(['User Type'])['User Type'].count()
    print('User Type count: ', ut_count)

    # TO DO: Display counts of gender
    try:
        g_count = df.groupby(['Gender'])['Gender'].count()
        print('Gender count: ', g_count)
    except KeyError:
        print('\n***KeyError: No gender data found!***')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birthyear = df['Birth Year'].min()
        max_birthyear = df['Birth Year'].max()
        c_birthyear = df['Birth Year'].mode()[0]
        print('\nMost earliest birth year: ', min_birthyear)
        print('Most recent birth year: ', max_birthyear)
        print('Most common birth year: ', c_birthyear)
    except:
        print('\n***KeyError: No birth year data found!***')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_disp(df):

    review_data = input('\nWould you like to review the raw data?\nEnter yes or no.\n')

    if review_data.lower() == 'yes':
        raw_data = df.head(5)
        print(raw_data)
        count = 5   # set counter at 5
        while True:

            add_five = input('\nWould you like to view an addtitional 5 records?\nEnter yes or no.\n')
            count = count + 5   # since 5 records have already been displayed the firs iteration will display 10

            if add_five.lower() == 'yes':
                add_data = df.head(count)
                print(add_data)
                continue
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_disp(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
