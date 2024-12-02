// Generated by gencpp from file iahrs_driver/euler_angle_resetResponse.msg
// DO NOT EDIT!


#ifndef IAHRS_DRIVER_MESSAGE_EULER_ANGLE_RESETRESPONSE_H
#define IAHRS_DRIVER_MESSAGE_EULER_ANGLE_RESETRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace iahrs_driver
{
template <class ContainerAllocator>
struct euler_angle_resetResponse_
{
  typedef euler_angle_resetResponse_<ContainerAllocator> Type;

  euler_angle_resetResponse_()
    : command_Result(false)  {
    }
  euler_angle_resetResponse_(const ContainerAllocator& _alloc)
    : command_Result(false)  {
  (void)_alloc;
    }



   typedef uint8_t _command_Result_type;
  _command_Result_type command_Result;





  typedef boost::shared_ptr< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> const> ConstPtr;

}; // struct euler_angle_resetResponse_

typedef ::iahrs_driver::euler_angle_resetResponse_<std::allocator<void> > euler_angle_resetResponse;

typedef boost::shared_ptr< ::iahrs_driver::euler_angle_resetResponse > euler_angle_resetResponsePtr;
typedef boost::shared_ptr< ::iahrs_driver::euler_angle_resetResponse const> euler_angle_resetResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator1> & lhs, const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator2> & rhs)
{
  return lhs.command_Result == rhs.command_Result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator1> & lhs, const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace iahrs_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6b370111df6d9d8116fbdd43bd394a52";
  }

  static const char* value(const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6b370111df6d9d81ULL;
  static const uint64_t static_value2 = 0x16fbdd43bd394a52ULL;
};

template<class ContainerAllocator>
struct DataType< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "iahrs_driver/euler_angle_resetResponse";
  }

  static const char* value(const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool command_Result\n"
"\n"
;
  }

  static const char* value(const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.command_Result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct euler_angle_resetResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::iahrs_driver::euler_angle_resetResponse_<ContainerAllocator>& v)
  {
    s << indent << "command_Result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.command_Result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IAHRS_DRIVER_MESSAGE_EULER_ANGLE_RESETRESPONSE_H
