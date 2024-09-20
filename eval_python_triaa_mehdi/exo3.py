class Exo:
    def puissance(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.puissance(x, -n)
        elif n % 2 == 0:
            moitié = self.puissance(x, n // 2)
            return moitié * moitié
        else:
            return x * self.puissance(x, n - 1)

# Exemple d'utilisation
e = Exo()
print(e.puissance(2, 3))  # 8
print(e.puissance(2, -3))  # 0.125
