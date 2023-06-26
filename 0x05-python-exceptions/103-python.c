#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	setbuf(stdout, NULL);
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	setbuf(stdout, NULL);
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i;

	printf("[.] bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first %ld bytes: ", size < 10 ? size : 10);
	for (i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x", ((PyBytesObject *)p)->ob_sval[i] & 0xff);
		if (i < (size < 10 ? size - 1 : 9))
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("[.] float object info\n");
	printf("  Value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
