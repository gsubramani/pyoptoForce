#include <pybind11/pybind11.h>
#include <omd/opto.h>
#include <pybind11/stl.h>




namespace py = pybind11;

PYBIND11_MAKE_OPAQUE(OPort*)

PYBIND11_PLUGIN(pyOptoForce) {
    py::module m("pyOptoForce", "Optoforce python bindings");
	

	py::class_<OptoPorts>(m, "OptoPorts")
		.def(py::init<int, int>())
		.def("getLastSize", &OptoPorts::getLastSize)
		.def("getSize", &OptoPorts::getSize)
		.def("listPorts",
			[](OptoPorts &ops,bool connectFilter) {
		OPort* start = ops.listPorts(connectFilter);
		OPort* end = ops.listPorts(connectFilter) + ops.getLastSize();
		return std::vector<OPort>(start,end);
	});
//		.def("listPorts", &OptoPorts::listPorts);

	py::class_<OptoPackage>(m, "OptoPackage")
		.def(py::init<>())
		.def_readonly("x", &OptoPackage::x)
		.def_readonly("y", &OptoPackage::y)
		.def_readonly("z", &OptoPackage::z);
	
	py::class_<OptoPackage6D>(m, "OptoPackage6D")
		.def(py::init<>())
		.def_readonly("Fx", &OptoPackage6D::Fx)
		.def_readonly("Fy", &OptoPackage6D::Fy)
		.def_readonly("Fz", &OptoPackage6D::Fz)
		.def_readonly("Tx", &OptoPackage6D::Tx)
		.def_readonly("Ty", &OptoPackage6D::Ty)
		.def_readonly("Tz", &OptoPackage6D::Tz);

	py::class_<OptoDAQ>(m, "OptoDAQ")
		.def(py::init<>())
//		.def("open_", [](OptoDAQ &daq, OPort* ops ,int index) {
//			return daq.open(ops[index]);
//		})
		.def("open", &OptoDAQ::open)
		.def("getVersion", &OptoDAQ::getVersion)
		.def("read", &OptoDAQ::read)
		.def("close", &OptoDAQ::close);

	py::class_<OPort>(m, "OPort")
		.def(py::init<>())
		.def("__repr__",
			[](const OPort &a) {
		return "<OPort: Device Name: " + std::string(a.deviceName) + "Serial Number: " + std::string(a.serialNumber) + ">"; });
	return m.ptr();
}
