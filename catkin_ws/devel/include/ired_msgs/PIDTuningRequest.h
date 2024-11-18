// Generated by gencpp from file ired_msgs/PIDTuningRequest.msg
// DO NOT EDIT!


#ifndef IRED_MSGS_MESSAGE_PIDTUNINGREQUEST_H
#define IRED_MSGS_MESSAGE_PIDTUNINGREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ired_msgs
{
template <class ContainerAllocator>
struct PIDTuningRequest_
{
  typedef PIDTuningRequest_<ContainerAllocator> Type;

  PIDTuningRequest_()
    : motor()
    , kp(0.0)
    , ki(0.0)
    , kd(0.0)  {
    }
  PIDTuningRequest_(const ContainerAllocator& _alloc)
    : motor(_alloc)
    , kp(0.0)
    , ki(0.0)
    , kd(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _motor_type;
  _motor_type motor;

   typedef double _kp_type;
  _kp_type kp;

   typedef double _ki_type;
  _ki_type ki;

   typedef double _kd_type;
  _kd_type kd;





  typedef boost::shared_ptr< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> const> ConstPtr;

}; // struct PIDTuningRequest_

typedef ::ired_msgs::PIDTuningRequest_<std::allocator<void> > PIDTuningRequest;

typedef boost::shared_ptr< ::ired_msgs::PIDTuningRequest > PIDTuningRequestPtr;
typedef boost::shared_ptr< ::ired_msgs::PIDTuningRequest const> PIDTuningRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ired_msgs::PIDTuningRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ired_msgs::PIDTuningRequest_<ContainerAllocator1> & lhs, const ::ired_msgs::PIDTuningRequest_<ContainerAllocator2> & rhs)
{
  return lhs.motor == rhs.motor &&
    lhs.kp == rhs.kp &&
    lhs.ki == rhs.ki &&
    lhs.kd == rhs.kd;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ired_msgs::PIDTuningRequest_<ContainerAllocator1> & lhs, const ::ired_msgs::PIDTuningRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ired_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2169d9d8246848be6270c046ce9df384";
  }

  static const char* value(const ::ired_msgs::PIDTuningRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2169d9d8246848beULL;
  static const uint64_t static_value2 = 0x6270c046ce9df384ULL;
};

template<class ContainerAllocator>
struct DataType< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ired_msgs/PIDTuningRequest";
  }

  static const char* value(const ::ired_msgs::PIDTuningRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string motor\n"
"float64 kp\n"
"float64 ki\n"
"float64 kd\n"
;
  }

  static const char* value(const ::ired_msgs::PIDTuningRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.motor);
      stream.next(m.kp);
      stream.next(m.ki);
      stream.next(m.kd);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PIDTuningRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ired_msgs::PIDTuningRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ired_msgs::PIDTuningRequest_<ContainerAllocator>& v)
  {
    s << indent << "motor: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.motor);
    s << indent << "kp: ";
    Printer<double>::stream(s, indent + "  ", v.kp);
    s << indent << "ki: ";
    Printer<double>::stream(s, indent + "  ", v.ki);
    s << indent << "kd: ";
    Printer<double>::stream(s, indent + "  ", v.kd);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IRED_MSGS_MESSAGE_PIDTUNINGREQUEST_H