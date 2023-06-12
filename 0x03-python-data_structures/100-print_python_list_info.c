#include <Python.h>

/**
 * print_python_list_info - print basic information about python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *list;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		list = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_Type(list)->tp_name);
	}
}
