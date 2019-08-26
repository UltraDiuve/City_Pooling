def city_max(city_dists):
    """
    Computes the max total distance amongst all cities
    """
    return(max(city_dists.values()))


"""
    Ce dont j'ai besoin. Pour une configuration :
    - Qu'elle présente un utilitaire qui sorte pour chaque ville les villes de
    la poule 1- dans la totalité
    - 2- avec uniquement un seul couple à chaque fois
    Pour le scoring, je peux faire un truc avec numpy ?
    1:[2] <= seq
    2:[1]
    3:[4]
    4:[3]
    {i:sum(ar[i:seq]) for i in range city_count}
    Mais pour ça il me faut déjà la fonction qui retourne la sequence pour
    chacun des nombres.
    ou bien je sommme par poule
"""
