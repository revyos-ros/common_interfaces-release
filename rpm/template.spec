%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-common-interfaces
Version:        4.2.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS common_interfaces package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-actionlib-msgs
Requires:       ros-humble-builtin-interfaces
Requires:       ros-humble-diagnostic-msgs
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-shape-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-std-srvs
Requires:       ros-humble-stereo-msgs
Requires:       ros-humble-trajectory-msgs
Requires:       ros-humble-visualization-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
common_interfaces contains messages and services that are widely used by other
ROS packages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu May 19 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.2-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.1-2
- Autogenerated by Bloom

* Thu Mar 31 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.1-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.2.0-1
- Autogenerated by Bloom

* Sat Mar 26 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.1.1-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Geoffrey Biggs <geoff@openrobotics.org> - 4.0.0-2
- Autogenerated by Bloom

