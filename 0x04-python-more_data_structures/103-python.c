#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid Python list object.\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *type = (PyObject *)p->ob_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the list = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *itemType = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, itemType);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Python bytes object.\n");
        return;
    }

    printf("[.] Bytes object info\n");
    printf("  Size: %zd\n", PyBytes_Size(p));
    printf("  Address of the object: %p\n", (void *)p);
    printf("  Bytes: ");
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t maxBytes = (size > 10) ? 10 : size;

    for (Py_ssize_t i = 0; i < maxBytes; i++) {
        printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
        if (i != maxBytes - 1)
            printf(" ");
    }

    printf("\n");
}

