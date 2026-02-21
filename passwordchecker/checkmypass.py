import requests
import hashlib
import sys


def requests_api_data(query_char):
    """
    The function `requests_api_data` fetches data from an API based on a given query character.

    :param query_char: The function `requests_api_data(query_char)` takes a single parameter
    `query_char`, which is used to construct a URL for making a request to the
    "https://api.pwnedpasswords.com/range/" API endpoint. The function then sends a GET request to the
    constructed URL and returns the
    :return: The function `requests_api_data(query_char)` returns the response object `res` after making
    a GET request to the specified URL.
    """
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching : {res.status_code}, check the API and try again"
        )
    return res


# def read_res(response):
#     print(response.text)


def get_pass_leaks_count(hashes, hash_to_check):
    """
    The function `get_pass_leaks_count` parses a list of hashes and returns the count associated with a
    specific hash to check.

    :param hashes: The `hashes` parameter is expected to be a text file containing lines of hash values
    and their corresponding counts separated by a colon (':'). Each line represents a hash value and its
    count
    :param hash_to_check: The `hash_to_check` parameter is the hash value that you want to check for in
    the list of hashes. The function `get_pass_leaks_count` takes two parameters: `hashes` which is a
    text containing hash values and their corresponding counts, and `hash_to_check` which is
    :return: the count of how many times the specified hash (hash_to_check) appears in the list of
    hashes. If the hash is found, the count is returned. If the hash is not found, the function returns
    0.
    """
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """
    The function `pwned_api_check` checks if a given password exists in an API response by hashing the
    password and making a request based on the hash.

    :param password: The `pwned_api_check` function takes a password as input, hashes it using SHA-1
    algorithm, sends the first 5 characters of the hashed password to an API to check for any leaks, and
    then returns the count of how many times the remaining characters of the hashed password appear in
    :return: The function `pwned_api_check` is returning the number of times the given password has been
    found in data breaches according to the API response.
    """
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    response = requests_api_data(first5char)
    # print(first5char, tail, response)
    return get_pass_leaks_count(response, tail)


# pwned_api_check("123")
# requests_api_data("123")


def main(args):
    """
    The function checks if passwords have been compromised using a pwned API and provides feedback on
    their security.

    :param args: The `args` parameter in the `main` function seems to be a list of passwords that are
    being checked for security using the `pwned_api_check` function. The function iterates over each
    password in the list, checks its security status, and then prints a message based on the result
    :return: the string "done".
    """
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... Think about changing your password "
            )
        else:
            print(f"{password} was not found Your password is secure")
        return "done"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
