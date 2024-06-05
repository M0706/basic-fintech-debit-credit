class Query:
    user_select_query = 'SELECT * FROM public."user" WHERE userid = $1'
    update_user_balance = 'UPDATE public."user" SET balance=$1 WHERE userid=$2'
    get_all_users_query = 'Select * from public."user"'
