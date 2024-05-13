def describe_7th_element():
    print("The '7th Element' song by Vitas is known for its unique style and energy.")
    print("It features rapid tempo and high-pitched vocals.")
    print("Vitas, a Ukrainian singer, gained international fame for his performance in this song.")
    print("The music video is surreal and often referenced in internet culture.")
    print("Overall, '7th Element' is a catchy and memorable piece.")

# Call the function to describe the song
describe_7th_element()
import webbrowser

def describe_7th_element():
    print("Welcome to the '7th Element' song description!")
    print("=============================================")
    print("The '7th Element' song by Vitas is known for its unique style and energy.")
    print("It was released in 2001 as part of Vitas' album 'Philosophy of Miracle'.")
    print("The song gained widespread attention on the internet due to its surreal music video and Vitas' remarkable vocal range.")
    print("Vitas' performance in the song features his signature countertenor voice, reaching incredibly high notes.")
    print("The lyrics of '7th Element' are in a mix of languages, including Russian and gibberish-like sounds, adding to its mystique.")
    print("The music video showcases elaborate visual effects and choreography, contributing to its viral popularity.")
    print("Despite being released years ago, '7th Element' continues to captivate audiences worldwide and remains a meme and internet sensation.")
    print("=============================================")
    play_song = input("Would you like to listen to a snippet of the song? (yes/no): ").lower()
    if play_song == "yes":
        play_snippet()
    rate_song()

def play_snippet():
    print("Playing a snippet of the '7th Element' song...")
    # Replace the URL with a link to the song or a snippet if available
    webbrowser.open("https://www.youtube.com/watch?v=b_Y7_zSXbAQ")

def rate_song():
    rating = input("How would you rate the '7th Element' song out of 5 stars? (1-5): ")
    try:
        rating = int(rating)
        if 1 <= rating <= 5:
            print("Thank you for rating the song!")
        else:
            print("Please enter a rating between 1 and 5.")
            rate_song()  # Ask for rating again
    except ValueError:
        print("Please enter a valid numeric rating.")
        rate_song()  # Ask for rating again

# Call the function to describe the song
describe_7th_element()
