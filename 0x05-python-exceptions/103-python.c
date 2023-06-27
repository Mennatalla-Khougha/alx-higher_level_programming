#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		char *type = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  Size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
		if (i < (size - 1))
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  Value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
