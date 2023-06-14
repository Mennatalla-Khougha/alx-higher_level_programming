#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - print bytes info
* @p: Python Object
*/
void print_python_bytes(PyObject *p)
{
	char *data;
	Py_ssize_t size, i, j;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyObject_Length(p);
	data = PyBytes_AsString(p);
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", data);
	if (size >= 10)
	{
		j = 10;
	}
	printf(" first %ld bytes: ", j);
	for (i = 0; i < j; i++)
	{
		if (data[i] >= 0)
		{
			printf("%02x", data[i]);
		}
		else
		{
			printf("%02x", 256 + data[i]);
		}
		printf("\n");
	}
}
/**
* print_python_list - print basic info about python list
* @p: python list
*/
void print_python_list(PyObject *p)
{
	py_ssize_t size, i;
	PyObject *item;

	size = PyObject_Length(p);
	printf("[*] Python list info\n");
	printf("[*] Size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->ob_alloc);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
	}
}
