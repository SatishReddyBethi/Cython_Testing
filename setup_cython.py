
# from setuptools import setup, find_packages, Extension # should be imported before Cython
# from Cython.Distutils import build_ext
# import numpy

# extensions = [
#     Extension("Extrusion_Functions_Cython", ["Cython/Extrusion_Functions_Cython.pyx"],
#         include_dirs=[numpy.get_include()])
# ]

# setup(
#     # name="My hello app",
#     ext_modules=cythonize(extensions,
#                         build_dir="build",
#                         compiler_directives={'language_level' : "3"},
#                         annotate=True
#                         )
# )

# setup(name='package',
#       packages=find_packages(),
#       cmdclass = {'build_ext': build_ext},
#       ext_modules = extensions,
#      )

# -------------------------- ALTERNATE SETUP ----------------------
from distutils.core import setup
from Cython.Build import cythonize
import numpy
import sys

# n_threads = 1

# if "-j" in sys.argv:
#     n_threads = int(sys.argv[sys.argv.index('-j')+1])
#     if n_threads > 1:
#         print(f"Building on [{n_threads}] threads")
#     elif not n_threads == 1:
#         n_threads = 1

print("====[Build Process Started]====")

setup(
    ext_modules = cythonize('Funcs_Cy.pyx',
                            compiler_directives={'language_level' : "3"},
                            build_dir="build",annotate=True), #nthreads=n_threads),
    # include_dirs=[numpy.get_include()]
    )

print("====[Build Successful]====")
# -------------------------- ALTERNATE SETUP 2---------------------
# from setuptools import setup
# from Cython.Build import cythonize
# from Cython.Distutils.extension import Extension
# import multiprocessing
# import sys
# import numpy

# NB_COMPILE_JOBS = 8

# EXTENSIONS = [Extension("Extrusion_Functions_Cython", ["Extrusion_Functions_Cython.pyx"],
#             include_dirs=[numpy.get_include()])]

# def setup_given_extensions(extensions):
#     setup(# name="My hello app",
#             ext_modules=cythonize(extensions,
#                         build_dir="build",
#                         compiler_directives={'language_level' : "3"},
#                         annotate=False))

# def setup_extensions_in_sequential():
#     setup_given_extensions(EXTENSIONS)

# def setup_extensions_in_parallel():
#     cythonize(EXTENSIONS, nthreads=NB_COMPILE_JOBS)
#     pool = multiprocessing.Pool(processes=NB_COMPILE_JOBS)
#     pool.map(setup_given_extensions, EXTENSIONS)
#     pool.close()
#     pool.join()

# if "build_ext" in sys.argv:
#     setup_extensions_in_parallel()
# else:
#     setup_extensions_in_sequential()

# ----------------- FOR MORE INFO ---------------------------------
# https://github.com/cython/cython/wiki/enhancements-distutils_preprocessing
# https://stackoverflow.com/questions/38013863/how-to-perform-cython-files-compilation-in-parallel
