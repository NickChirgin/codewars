start = ["http://", "https://", "www."]
def domain_name(url):
    index = 0
    for i in start:
        if i in url:
            url = url.replace(i, "")
    for dot in url:
        if dot == ".":
            index = url.index(dot)
            url = url[:index]
            break
    return url

print(domain_name("http://github.com/carbonfive/raygun"))