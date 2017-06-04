# How you can see function "create is qv" create new function
# that for geted prime chose quadratic or not residue
#
#
def create_is_qv(n):
    def is_Quadratic_residue(k):
        return (k**((n-1)//2))%n == 1
    return is_Quadratic_residue
if __name__ == "__main__":
    list_of_is = []
    for i in [5,7,13]:
        list_of_is.append(create_is_qv(i))
    for func in list_of_is:
        assert func(1) == True, "Mistake in is_quadratic_residue"
