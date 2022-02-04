
pkgname=Encd
pkgver=1.0
pkgrel=1
pkgdesc="Encryption-De"
arch=("any")
url="https://github.com/stupid-kid-af/Encrypt-Decrypt-PyQt5"
license=("GPL3")
makedepends=('python-setuptools')

build() {
    python setup.py build
}

package() {
    python setup.py install --root="$pkgdir" --optimize=1
}
