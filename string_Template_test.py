from string import Template

# format() method is good but You need more secure way, use Template

def main():
    #usual string formatting with format()
    str1="You're watching {0} by {1}".format("Advanced Python", "Ercan Karacelik")
    print(str1)

    #Create temlate with placeholders
    templ=Template("You're watching ${title} by ${author}")
    str2= templ.substitute(title="Advenced Python", author="Joe Maini")
    print(str2)

    #use substitude method with a dictionary
    data= {
        "author":"Ercan Karacelik",
        "title":"Advenced Python"
    }
    str3=templ.substitute(data)
    print(str3)


if __name__=="__main__":
    main()
