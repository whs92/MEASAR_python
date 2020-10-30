TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC += measar

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install measar.dbd into <top>/dbd
DBD += measar.dbd

# specify all source files to be compiled and added to the library
#measar_SRCS += xxx

measar_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

