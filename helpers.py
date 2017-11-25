from flask import session
from werkzeug.security import check_password_hash
from dbconnection import getConnection

def logIn(username: str, password: str) -> bool:
    """Attempt to log a user in

    Uses the given plaintext username and password and tries to log the user in.
    If it succeeds, it adds the userid to the session with the key 'userid' and
    returns True. Otherwise, it only returns False
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # SQL Query
    statement = 'SELECT * FROM Users WHERE username = %s'
    cursor.execute(statement, (username,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we only expect to have one, since username is unique
    result = cursor.fetchall()
    if len(result) != 1:
        return(False)
    result = result[0]

    # Check the password
    if not check_password_hash(result[3].decode(), password):
        return(False)

    # Set session values and return
    session['userid'] = result[0]
    return(True)

def getSets(userid:int) -> dictionary:
    """Take the userid, display all sets in his account

    If successfully read the sets, return true, else return false
    If the user clicked on 1 set, display it
    """
    pass

def getCards(userid:int, setid:int):
    """Get all cards with a specific userid in a set

    Get all cards in the set and filter the ones with the userid
    """
    pass

def addCard(cardFront = '':str, cardBack = '':str, setid:int) -> bool
    """Add a new card  to the table

    Take the information on a card's front and back side, insert it to Cards table and assign a set to it
    If successfully added it, return true, else return false
    """
    pass

def editCard(cardid:int, cardFront:str, cardBack:str) -> bool
    """Edit a card's information

    Edit a card's information, include the context on frontside, backside and the setid
    If successfully edited it, return true, else return false
    """
    pass

def deleteCard(cardid:id) -> bool
    """Delete a card from Cards table

    If successfully deleted it, return true, else return false
    """
    pass

def indicateCard(cardid:int, answer:int = 0) -> bool
    """Set the indicator to 0 or 1

    Take a cardid and a number which needs to be 0 or 1
    Set the card's indicator to the number
    If successfully changed it's value, return true, else return false
    """
    pass

def addCategory(categoryName:str) -> bool
    """Add a new category

    Take the category's name and userid session variable, add it to the Category table
    If successfully added it to the table, return true, else return false
    """
    pass

def addSet(setName:str, categoryid:int) -> bool
    """Add a new set

    Take the set's name , categoryid and userid session variable, add it to the Sets table
    If didn't 
    If successfully added it to the table, return true, else return false
    """
    pass

def modifySet(setig:int, newName:str) -> bool
    """Modify a set

    Change the set's name
    If successfully changed the name, return true, else return false
    """
    pass

def modifyCategory(categoryid:int, newName:str) -> bool
    """Modify a category

    Change the category's name
    If successfully changed the name, return true, else return false
    """
    pass

def deleteSets(setid:int) -> bool
    """Delete all information in a set

    Delete everything in a set, include idname, categoryid, userid and create date
    If successfully reset the set, return true, else return false
    """
    pass

def deleteCategory(categoryid: int) -> bool
    """Delete a category

    Delete everything in a category, includ id, userid, name
    If successfully reset the set, return true, else return falsee
    """
    pass

def signiOut() -> bool
    """Sign out the user

    Sign out the user and redirect to the login page
    If successfully sing out the user, return true, else return false
    """
    pass
