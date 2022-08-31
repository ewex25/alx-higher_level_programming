#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - gives data of the PyBytesObject
 *
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
  Py_ssize_t syz = 0, n = 0;
  char *strng = NULL;

  printf("[.] bytes object info\n");

  if (!PyBytes_CheckExact(p))
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  if (PyBytes_AsStringAndSize(p, &strng, &syz) != -1)
    {
      printf("  size: %zd\n", syz);
      printf("  trying string: %s\n", strng);
      printf("  first %zd bytes:", syz < 10 ? syz + 1 : 10);
      while (n < syz + 1 && n < 10)
	{
	  printf(" %02hhx", strng[n]);
	  n++;
	}
      printf("\n");
    }
}

/**
 * print_python_list - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *f)
{
  Py_ssize_t syz = 0;
  PyObject *itm;
  int n = 0;

  if (PyList_CheckExact(f))
    {
      syz = PyList_Size(f);

      printf("[*] Python list info\n");
      printf("[*] Size of the Python List = %zd\n", syz);
      printf("[*] Allocated = %lu\n", ((PyListObject *)f)->allocated);

      while (n < syz)
	{
	  itm = PyList_GET_ITEM(f, n);
	  printf("Element %d: %s\n", n, itm->ob_type->tp_name);
	  if (PyBytes_Check(itm))
	    print_python_bytes(itm);
	  n++;
	}
    }
}
