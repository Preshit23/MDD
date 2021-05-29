import webbrowser
def search(species):
    url = 'https://www.google.com/search?q=' + species + ' uses and properties'
    url = url.replace(' ', '+')
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)