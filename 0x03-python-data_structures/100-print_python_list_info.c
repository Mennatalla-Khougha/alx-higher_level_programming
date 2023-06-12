#include <Python.h>

/**
 * print_python_list_info - print basic information about python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *list;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		list = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(list)->tp_name);
	}
}
