import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    filter_men = df['sex'] == 'Male'
    average_age_men = round(df[filter_men]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    filter_edu = df['education'] == 'Bachelors'
    bachelors = df[filter_edu]['education'].count()
    all_peeps = df['education'].count()
    percentage_bachelors = round(bachelors/all_peeps * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ((df['education'] == 'Bachelors') |
                        (df['education'] == 'Masters') |
                        (df['education'] == 'Doctorate'))
    #returns all salaries greater than 50K
    filter_sal = df['salary'] == '>50K'
    #returns the count salaries of all people with Bachelors, Masters, and Doctorates
    high_salary = df[higher_education]['salary'].count()
    low_salary = df[~higher_education]['salary'].count()
    # percentage with salary >50K
    higher_education_rich = round(
        df[higher_education].loc[filter_sal]['salary'].count() / high_salary *
        100, 1)
    lower_education_rich = round(
        df[~higher_education].loc[filter_sal]['salary'].count() / low_salary *
        100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #since this is a number and not a dataset, I have to set column hours per week equal to min_work_hours
    hpw = df['hours-per-week'] == min_work_hours
    hpw_salary = df[hpw]['salary'].count()
    rich_percentage = round(
        df[hpw].loc[filter_sal]['salary'].count() / hpw_salary * 100, 1)


    # What country has the highest percentage of people that earn >50K?
    nc_high = df['native-country'][filter_sal].value_counts()
    nc_total = df['native-country'].value_counts()
    nc_percent= round(nc_high/nc_total *100, 1)
    #idxmax() returns indices labels, not integers.
    highest_earning_country = nc_percent.idxmax()
    highest_earning_country_percentage = nc_percent.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india = df['native-country'] == 'India'
    top_IN_occupation = df[india].loc[filter_sal]['occupation'].mode().item()


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:\n",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country:\n {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
