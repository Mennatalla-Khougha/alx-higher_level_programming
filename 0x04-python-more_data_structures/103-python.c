#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *data;
	long int size, i, j;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	data = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	if (size >= 10)
		j = 10;
	else
		j = size + 1;

	printf("  first %ld bytes:", j);

	for (i = 0; i < j; i++)
		if (data[i] >= 0)
			printf(" %02x", data[i]);
		else
			printf(" %02x", 256 + data[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
