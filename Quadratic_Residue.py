# How you can see function "cr_is_quad" creates function
# for obtained prime. That function obtains number and return True if number is quadratic residue under modul of that prime
# and False in other case
#
def cr_is_quad(p):
    def is_quadratic_residue(k):
        return (k**((p-1)//2))%p == 1
    return is_quadratic_residue
if __name__ == "__main__":
    list_of_is = []
    for i in [5,7,13]:
        list_of_is.append(cr_is_quad(i))
    for func in list_of_is:
        assert func(1) == True, "Mistake in is_quadratic_residue"
