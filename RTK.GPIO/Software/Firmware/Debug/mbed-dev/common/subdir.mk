################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../mbed-dev/common/assert.c \
../mbed-dev/common/board.c \
../mbed-dev/common/error.c \
../mbed-dev/common/gpio.c \
../mbed-dev/common/lp_ticker_api.c \
../mbed-dev/common/mbed_interface.c \
../mbed-dev/common/pinmap_common.c \
../mbed-dev/common/rtc_time.c \
../mbed-dev/common/semihost_api.c \
../mbed-dev/common/ticker_api.c \
../mbed-dev/common/us_ticker_api.c \
../mbed-dev/common/wait_api.c 

CPP_SRCS += \
../mbed-dev/common/BusIn.cpp \
../mbed-dev/common/BusInOut.cpp \
../mbed-dev/common/BusOut.cpp \
../mbed-dev/common/CAN.cpp \
../mbed-dev/common/CallChain.cpp \
../mbed-dev/common/Ethernet.cpp \
../mbed-dev/common/FileBase.cpp \
../mbed-dev/common/FileLike.cpp \
../mbed-dev/common/FilePath.cpp \
../mbed-dev/common/FileSystemLike.cpp \
../mbed-dev/common/I2C.cpp \
../mbed-dev/common/I2CSlave.cpp \
../mbed-dev/common/InterruptIn.cpp \
../mbed-dev/common/InterruptManager.cpp \
../mbed-dev/common/LocalFileSystem.cpp \
../mbed-dev/common/RawSerial.cpp \
../mbed-dev/common/SPI.cpp \
../mbed-dev/common/SPISlave.cpp \
../mbed-dev/common/Serial.cpp \
../mbed-dev/common/SerialBase.cpp \
../mbed-dev/common/Stream.cpp \
../mbed-dev/common/Ticker.cpp \
../mbed-dev/common/Timeout.cpp \
../mbed-dev/common/Timer.cpp \
../mbed-dev/common/TimerEvent.cpp \
../mbed-dev/common/retarget.cpp 

OBJS += \
./mbed-dev/common/BusIn.o \
./mbed-dev/common/BusInOut.o \
./mbed-dev/common/BusOut.o \
./mbed-dev/common/CAN.o \
./mbed-dev/common/CallChain.o \
./mbed-dev/common/Ethernet.o \
./mbed-dev/common/FileBase.o \
./mbed-dev/common/FileLike.o \
./mbed-dev/common/FilePath.o \
./mbed-dev/common/FileSystemLike.o \
./mbed-dev/common/I2C.o \
./mbed-dev/common/I2CSlave.o \
./mbed-dev/common/InterruptIn.o \
./mbed-dev/common/InterruptManager.o \
./mbed-dev/common/LocalFileSystem.o \
./mbed-dev/common/RawSerial.o \
./mbed-dev/common/SPI.o \
./mbed-dev/common/SPISlave.o \
./mbed-dev/common/Serial.o \
./mbed-dev/common/SerialBase.o \
./mbed-dev/common/Stream.o \
./mbed-dev/common/Ticker.o \
./mbed-dev/common/Timeout.o \
./mbed-dev/common/Timer.o \
./mbed-dev/common/TimerEvent.o \
./mbed-dev/common/assert.o \
./mbed-dev/common/board.o \
./mbed-dev/common/error.o \
./mbed-dev/common/gpio.o \
./mbed-dev/common/lp_ticker_api.o \
./mbed-dev/common/mbed_interface.o \
./mbed-dev/common/pinmap_common.o \
./mbed-dev/common/retarget.o \
./mbed-dev/common/rtc_time.o \
./mbed-dev/common/semihost_api.o \
./mbed-dev/common/ticker_api.o \
./mbed-dev/common/us_ticker_api.o \
./mbed-dev/common/wait_api.o 

C_DEPS += \
./mbed-dev/common/assert.d \
./mbed-dev/common/board.d \
./mbed-dev/common/error.d \
./mbed-dev/common/gpio.d \
./mbed-dev/common/lp_ticker_api.d \
./mbed-dev/common/mbed_interface.d \
./mbed-dev/common/pinmap_common.d \
./mbed-dev/common/rtc_time.d \
./mbed-dev/common/semihost_api.d \
./mbed-dev/common/ticker_api.d \
./mbed-dev/common/us_ticker_api.d \
./mbed-dev/common/wait_api.d 

CPP_DEPS += \
./mbed-dev/common/BusIn.d \
./mbed-dev/common/BusInOut.d \
./mbed-dev/common/BusOut.d \
./mbed-dev/common/CAN.d \
./mbed-dev/common/CallChain.d \
./mbed-dev/common/Ethernet.d \
./mbed-dev/common/FileBase.d \
./mbed-dev/common/FileLike.d \
./mbed-dev/common/FilePath.d \
./mbed-dev/common/FileSystemLike.d \
./mbed-dev/common/I2C.d \
./mbed-dev/common/I2CSlave.d \
./mbed-dev/common/InterruptIn.d \
./mbed-dev/common/InterruptManager.d \
./mbed-dev/common/LocalFileSystem.d \
./mbed-dev/common/RawSerial.d \
./mbed-dev/common/SPI.d \
./mbed-dev/common/SPISlave.d \
./mbed-dev/common/Serial.d \
./mbed-dev/common/SerialBase.d \
./mbed-dev/common/Stream.d \
./mbed-dev/common/Ticker.d \
./mbed-dev/common/Timeout.d \
./mbed-dev/common/Timer.d \
./mbed-dev/common/TimerEvent.d \
./mbed-dev/common/retarget.d 


# Each subdirectory must supply rules for building sources it contributes
mbed-dev/common/%.o: ../mbed-dev/common/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: MCU G++ Compiler'
	@echo $(PWD)
	arm-none-eabi-g++ -mcpu=cortex-m0 -mthumb -mfloat-abi=soft -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTINOUT=1 -D__MBED_CMSIS_RTOS_CM -DTARGET_STM32F0 -DDEVICE_RTC=1 -DTOOLCHAIN_object -DTARGET_NUCLEO_F030R8 -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DTARGET_CORTEX_M -DARM_MATH_CM0 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_M0 -DDEVICE_SERIAL=1 -DDEVICE_INTERRUPTIN=1 -D__CORTEX_M0 -DDEVICE_I2C=1 -DDEVICE_PORTOUT=1 -DDEVICE_STDIO_MESSAGES=1 -DMBED_BUILD_TIMESTAMP=1473017828.47 -DTARGET_FF_MORPHO -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DTARGET_RELEASE -DTARGET_STM -DDEVICE_PORTIN=1 -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_SPI=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_STM32F030R8 -DTARGET_LIKE_CORTEX_M0 -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/." -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/SoftPWM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/api" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal/storage_abstraction" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8/TOOLCHAIN_GCC_ARM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/common" -Og -g3 -Wall -fmessage-length=0 -ffunction-sections -c -fno-exceptions -fno-rtti -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

mbed-dev/common/%.o: ../mbed-dev/common/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU GCC Compiler'
	@echo $(PWD)
	arm-none-eabi-gcc -mcpu=cortex-m0 -mthumb -mfloat-abi=soft -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTINOUT=1 -D__MBED_CMSIS_RTOS_CM -DTARGET_STM32F0 -DDEVICE_RTC=1 -DTOOLCHAIN_object -DTARGET_NUCLEO_F030R8 -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DTARGET_CORTEX_M -DARM_MATH_CM0 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_M0 -DDEVICE_SERIAL=1 -DDEVICE_INTERRUPTIN=1 -D__CORTEX_M0 -DDEVICE_I2C=1 -DDEVICE_PORTOUT=1 -DDEVICE_STDIO_MESSAGES=1 -DMBED_BUILD_TIMESTAMP=1473017828.47 -DTARGET_FF_MORPHO -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DTARGET_RELEASE -DTARGET_STM -DDEVICE_PORTIN=1 -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_SPI=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_STM32F030R8 -DTARGET_LIKE_CORTEX_M0 -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/." -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/SoftPWM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/api" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal/storage_abstraction" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8/TOOLCHAIN_GCC_ARM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/common" -Og -g3 -Wall -fmessage-length=0 -ffunction-sections -c -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


