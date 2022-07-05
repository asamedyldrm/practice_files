def greet():

    def good_morning(name):
        print("Günaydın", name)

    # good_morning()
    return good_morning

fn = greet()
fn("Samet")